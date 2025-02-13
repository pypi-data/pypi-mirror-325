import { i as pe, a as B, r as me, g as _e, w as j, d as ge, b as O, c as he } from "./Index-C5dC8F2H.js";
const E = window.ms_globals.React, N = window.ms_globals.React.useMemo, re = window.ms_globals.React.useState, oe = window.ms_globals.React.useEffect, de = window.ms_globals.React.forwardRef, fe = window.ms_globals.React.useRef, U = window.ms_globals.ReactDOM.createPortal, be = window.ms_globals.internalContext.useContextPropsContext, K = window.ms_globals.internalContext.ContextPropsProvider, k = window.ms_globals.antd.Typography;
var ye = /\s/;
function xe(e) {
  for (var t = e.length; t-- && ye.test(e.charAt(t)); )
    ;
  return t;
}
var Ce = /^\s+/;
function we(e) {
  return e && e.slice(0, xe(e) + 1).replace(Ce, "");
}
var V = NaN, Ee = /^[-+]0x[0-9a-f]+$/i, Ie = /^0b[01]+$/i, ve = /^0o[0-7]+$/i, Se = parseInt;
function q(e) {
  if (typeof e == "number")
    return e;
  if (pe(e))
    return V;
  if (B(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = B(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = we(e);
  var r = Ie.test(e);
  return r || ve.test(e) ? Se(e.slice(2), r ? 2 : 8) : Ee.test(e) ? V : +e;
}
var M = function() {
  return me.Date.now();
}, Te = "Expected a function", Re = Math.max, Oe = Math.min;
function ke(e, t, r) {
  var s, i, n, o, l, c, g = 0, h = !1, a = !1, x = !0;
  if (typeof e != "function")
    throw new TypeError(Te);
  t = q(t) || 0, B(r) && (h = !!r.leading, a = "maxWait" in r, n = a ? Re(q(r.maxWait) || 0, t) : n, x = "trailing" in r ? !!r.trailing : x);
  function p(d) {
    var y = s, w = i;
    return s = i = void 0, g = d, o = e.apply(w, y), o;
  }
  function C(d) {
    return g = d, l = setTimeout(_, t), h ? p(d) : o;
  }
  function f(d) {
    var y = d - c, w = d - g, H = t - y;
    return a ? Oe(H, n - w) : H;
  }
  function m(d) {
    var y = d - c, w = d - g;
    return c === void 0 || y >= t || y < 0 || a && w >= n;
  }
  function _() {
    var d = M();
    if (m(d))
      return I(d);
    l = setTimeout(_, f(d));
  }
  function I(d) {
    return l = void 0, x && s ? p(d) : (s = i = void 0, o);
  }
  function v() {
    l !== void 0 && clearTimeout(l), g = 0, s = c = i = l = void 0;
  }
  function u() {
    return l === void 0 ? o : I(M());
  }
  function S() {
    var d = M(), y = m(d);
    if (s = arguments, i = this, c = d, y) {
      if (l === void 0)
        return C(c);
      if (a)
        return clearTimeout(l), l = setTimeout(_, t), p(c);
    }
    return l === void 0 && (l = setTimeout(_, t)), o;
  }
  return S.cancel = v, S.flush = u, S;
}
var se = {
  exports: {}
}, W = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Pe = E, je = Symbol.for("react.element"), Le = Symbol.for("react.fragment"), Ae = Object.prototype.hasOwnProperty, Ne = Pe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, We = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ie(e, t, r) {
  var s, i = {}, n = null, o = null;
  r !== void 0 && (n = "" + r), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (o = t.ref);
  for (s in t) Ae.call(t, s) && !We.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: je,
    type: e,
    key: n,
    ref: o,
    props: i,
    _owner: Ne.current
  };
}
W.Fragment = Le;
W.jsx = ie;
W.jsxs = ie;
se.exports = W;
var b = se.exports;
const {
  SvelteComponent: Me,
  assign: J,
  binding_callbacks: X,
  check_outros: De,
  children: le,
  claim_element: ae,
  claim_space: Fe,
  component_subscribe: Y,
  compute_slots: Ue,
  create_slot: Be,
  detach: R,
  element: ce,
  empty: Q,
  exclude_internal_props: Z,
  get_all_dirty_from_scope: ze,
  get_slot_changes: Ge,
  group_outros: He,
  init: Ke,
  insert_hydration: L,
  safe_not_equal: Ve,
  set_custom_element_data: ue,
  space: qe,
  transition_in: A,
  transition_out: z,
  update_slot_base: Je
} = window.__gradio__svelte__internal, {
  beforeUpdate: Xe,
  getContext: Ye,
  onDestroy: Qe,
  setContext: Ze
} = window.__gradio__svelte__internal;
function $(e) {
  let t, r;
  const s = (
    /*#slots*/
    e[7].default
  ), i = Be(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ce("svelte-slot"), i && i.c(), this.h();
    },
    l(n) {
      t = ae(n, "SVELTE-SLOT", {
        class: !0
      });
      var o = le(t);
      i && i.l(o), o.forEach(R), this.h();
    },
    h() {
      ue(t, "class", "svelte-1rt0kpf");
    },
    m(n, o) {
      L(n, t, o), i && i.m(t, null), e[9](t), r = !0;
    },
    p(n, o) {
      i && i.p && (!r || o & /*$$scope*/
      64) && Je(
        i,
        s,
        n,
        /*$$scope*/
        n[6],
        r ? Ge(
          s,
          /*$$scope*/
          n[6],
          o,
          null
        ) : ze(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      r || (A(i, n), r = !0);
    },
    o(n) {
      z(i, n), r = !1;
    },
    d(n) {
      n && R(t), i && i.d(n), e[9](null);
    }
  };
}
function $e(e) {
  let t, r, s, i, n = (
    /*$$slots*/
    e[4].default && $(e)
  );
  return {
    c() {
      t = ce("react-portal-target"), r = qe(), n && n.c(), s = Q(), this.h();
    },
    l(o) {
      t = ae(o, "REACT-PORTAL-TARGET", {
        class: !0
      }), le(t).forEach(R), r = Fe(o), n && n.l(o), s = Q(), this.h();
    },
    h() {
      ue(t, "class", "svelte-1rt0kpf");
    },
    m(o, l) {
      L(o, t, l), e[8](t), L(o, r, l), n && n.m(o, l), L(o, s, l), i = !0;
    },
    p(o, [l]) {
      /*$$slots*/
      o[4].default ? n ? (n.p(o, l), l & /*$$slots*/
      16 && A(n, 1)) : (n = $(o), n.c(), A(n, 1), n.m(s.parentNode, s)) : n && (He(), z(n, 1, 1, () => {
        n = null;
      }), De());
    },
    i(o) {
      i || (A(n), i = !0);
    },
    o(o) {
      z(n), i = !1;
    },
    d(o) {
      o && (R(t), R(r), R(s)), e[8](null), n && n.d(o);
    }
  };
}
function ee(e) {
  const {
    svelteInit: t,
    ...r
  } = e;
  return r;
}
function et(e, t, r) {
  let s, i, {
    $$slots: n = {},
    $$scope: o
  } = t;
  const l = Ue(n);
  let {
    svelteInit: c
  } = t;
  const g = j(ee(t)), h = j();
  Y(e, h, (u) => r(0, s = u));
  const a = j();
  Y(e, a, (u) => r(1, i = u));
  const x = [], p = Ye("$$ms-gr-react-wrapper"), {
    slotKey: C,
    slotIndex: f,
    subSlotIndex: m
  } = _e() || {}, _ = c({
    parent: p,
    props: g,
    target: h,
    slot: a,
    slotKey: C,
    slotIndex: f,
    subSlotIndex: m,
    onDestroy(u) {
      x.push(u);
    }
  });
  Ze("$$ms-gr-react-wrapper", _), Xe(() => {
    g.set(ee(t));
  }), Qe(() => {
    x.forEach((u) => u());
  });
  function I(u) {
    X[u ? "unshift" : "push"](() => {
      s = u, h.set(s);
    });
  }
  function v(u) {
    X[u ? "unshift" : "push"](() => {
      i = u, a.set(i);
    });
  }
  return e.$$set = (u) => {
    r(17, t = J(J({}, t), Z(u))), "svelteInit" in u && r(5, c = u.svelteInit), "$$scope" in u && r(6, o = u.$$scope);
  }, t = Z(t), [s, i, h, a, l, c, o, n, I, v];
}
class tt extends Me {
  constructor(t) {
    super(), Ke(this, t, et, $e, Ve, {
      svelteInit: 5
    });
  }
}
const te = window.ms_globals.rerender, D = window.ms_globals.tree;
function nt(e, t = {}) {
  function r(s) {
    const i = j(), n = new tt({
      ...s,
      props: {
        svelteInit(o) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: e,
            props: o.props,
            slot: o.slot,
            target: o.target,
            slotIndex: o.slotIndex,
            subSlotIndex: o.subSlotIndex,
            ignore: t.ignore,
            slotKey: o.slotKey,
            nodes: []
          }, c = o.parent ?? D;
          return c.nodes = [...c.nodes, l], te({
            createPortal: U,
            node: D
          }), o.onDestroy(() => {
            c.nodes = c.nodes.filter((g) => g.svelteInstance !== i), te({
              createPortal: U,
              node: D
            });
          }), l;
        },
        ...s.props
      }
    });
    return i.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(r);
    });
  });
}
function rt(e) {
  const [t, r] = re(() => O(e));
  return oe(() => {
    let s = !0;
    return e.subscribe((n) => {
      s && (s = !1, n === t) || r(n);
    });
  }, [e]), t;
}
function ot(e) {
  const t = N(() => ge(e, (r) => r), [e]);
  return rt(t);
}
const st = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function it(e) {
  return e ? Object.keys(e).reduce((t, r) => {
    const s = e[r];
    return t[r] = lt(r, s), t;
  }, {}) : {};
}
function lt(e, t) {
  return typeof t == "number" && !st.includes(e) ? t + "px" : t;
}
function G(e) {
  const t = [], r = e.cloneNode(!1);
  if (e._reactElement) {
    const i = E.Children.toArray(e._reactElement.props.children).map((n) => {
      if (E.isValidElement(n) && n.props.__slot__) {
        const {
          portals: o,
          clonedElement: l
        } = G(n.props.el);
        return E.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...E.Children.toArray(n.props.children), ...o]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(U(E.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), r)), {
      clonedElement: r,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: o,
      type: l,
      useCapture: c
    }) => {
      r.addEventListener(l, o, c);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const n = s[i];
    if (n.nodeType === 1) {
      const {
        clonedElement: o,
        portals: l
      } = G(n);
      t.push(...l), r.appendChild(o);
    } else n.nodeType === 3 && r.appendChild(n.cloneNode());
  }
  return {
    clonedElement: r,
    portals: t
  };
}
function at(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const T = de(({
  slot: e,
  clone: t,
  className: r,
  style: s,
  observeAttributes: i
}, n) => {
  const o = fe(), [l, c] = re([]), {
    forceClone: g
  } = be(), h = g ? !0 : t;
  return oe(() => {
    var C;
    if (!o.current || !e)
      return;
    let a = e;
    function x() {
      let f = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (f = a.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), at(n, f), r && f.classList.add(...r.split(" ")), s) {
        const m = it(s);
        Object.keys(m).forEach((_) => {
          f.style[_] = m[_];
        });
      }
    }
    let p = null;
    if (h && window.MutationObserver) {
      let f = function() {
        var v, u, S;
        (v = o.current) != null && v.contains(a) && ((u = o.current) == null || u.removeChild(a));
        const {
          portals: _,
          clonedElement: I
        } = G(e);
        a = I, c(_), a.style.display = "contents", x(), (S = o.current) == null || S.appendChild(a);
      };
      f();
      const m = ke(() => {
        f(), p == null || p.disconnect(), p == null || p.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      p = new window.MutationObserver(m), p.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      a.style.display = "contents", x(), (C = o.current) == null || C.appendChild(a);
    return () => {
      var f, m;
      a.style.display = "", (f = o.current) != null && f.contains(a) && ((m = o.current) == null || m.removeChild(a)), p == null || p.disconnect();
    };
  }, [e, h, r, s, n, i]), E.createElement("react-child", {
    ref: o,
    style: {
      display: "contents"
    }
  }, ...l);
});
function ct(e) {
  return N(() => {
    const t = E.Children.toArray(e), r = [], s = [];
    return t.forEach((i) => {
      i.props.node && i.props.nodeSlotKey ? r.push(i) : s.push(i);
    }), [r, s];
  }, [e]);
}
function F(e, t) {
  const r = N(() => E.Children.toArray(e.originalChildren || e).filter((n) => n.props.node && !n.props.node.ignore && (!t && !n.props.nodeSlotKey || t && t === n.props.nodeSlotKey)).sort((n, o) => {
    if (n.props.node.slotIndex && o.props.node.slotIndex) {
      const l = O(n.props.node.slotIndex) || 0, c = O(o.props.node.slotIndex) || 0;
      return l - c === 0 && n.props.node.subSlotIndex && o.props.node.subSlotIndex ? (O(n.props.node.subSlotIndex) || 0) - (O(o.props.node.subSlotIndex) || 0) : l - c;
    }
    return 0;
  }).map((n) => n.props.node.target), [e, t]);
  return ot(r);
}
function ut(e) {
  return Object.keys(e).reduce((t, r) => (e[r] !== void 0 && (t[r] = e[r]), t), {});
}
function ne(e, t) {
  return e ? /* @__PURE__ */ b.jsx(T, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function dt({
  key: e,
  slots: t,
  targets: r
}, s) {
  return t[e] ? (...i) => r ? r.map((n, o) => /* @__PURE__ */ b.jsx(K, {
    params: i,
    forceClone: (s == null ? void 0 : s.forceClone) ?? !0,
    children: ne(n, {
      clone: !0,
      ...s
    })
  }, o)) : /* @__PURE__ */ b.jsx(K, {
    params: i,
    forceClone: (s == null ? void 0 : s.forceClone) ?? !0,
    children: ne(t[e], {
      clone: !0,
      ...s
    })
  }) : void 0;
}
function P(e) {
  return typeof e == "object" && e !== null ? e : {};
}
const pt = nt(({
  component: e,
  className: t,
  slots: r,
  children: s,
  copyable: i,
  editable: n,
  ellipsis: o,
  setSlotParams: l,
  value: c,
  ...g
}) => {
  var d;
  const h = F(s, "copyable.tooltips"), a = F(s, "copyable.icon"), x = r["copyable.icon"] || h.length > 0 || i, p = r["editable.icon"] || r["editable.tooltip"] || r["editable.enterIcon"] || n, C = r["ellipsis.symbol"] || r["ellipsis.tooltip"] || r["ellipsis.tooltip.title"] || o, f = P(i), m = P(n), _ = P(o), I = N(() => {
    switch (e) {
      case "title":
        return k.Title;
      case "paragraph":
        return k.Paragraph;
      case "text":
        return k.Text;
      case "link":
        return k.Link;
    }
  }, [e]), [v, u] = ct(s), S = F(s);
  return /* @__PURE__ */ b.jsxs(b.Fragment, {
    children: [/* @__PURE__ */ b.jsx("div", {
      style: {
        display: "none"
      },
      children: v
    }), /* @__PURE__ */ b.jsx(I, {
      ...g,
      className: he(t, `ms-gr-antd-typography-${e}`),
      copyable: x ? ut({
        text: c,
        ...P(i),
        tooltips: h.length > 0 ? h.map((y, w) => /* @__PURE__ */ b.jsx(T, {
          slot: y
        }, w)) : f.tooltips,
        icon: a.length > 0 ? a.map((y, w) => /* @__PURE__ */ b.jsx(T, {
          slot: y,
          clone: !0
        }, w)) : f.icon
      }) : void 0,
      editable: p ? {
        ...m,
        icon: r["editable.icon"] ? /* @__PURE__ */ b.jsx(T, {
          slot: r["editable.icon"],
          clone: !0
        }) : m.icon,
        tooltip: r["editable.tooltip"] ? /* @__PURE__ */ b.jsx(T, {
          slot: r["editable.tooltip"]
        }) : m.tooltip,
        enterIcon: r["editable.enterIcon"] ? /* @__PURE__ */ b.jsx(T, {
          slot: r["editable.enterIcon"]
        }) : m.enterIcon
      } : void 0,
      ellipsis: e === "link" ? !!C : C ? {
        ..._,
        symbol: r["ellipsis.symbol"] ? dt({
          key: "ellipsis.symbol",
          setSlotParams: l,
          slots: r
        }, {
          clone: !0
        }) : _.symbol,
        tooltip: r["ellipsis.tooltip"] ? /* @__PURE__ */ b.jsx(T, {
          slot: r["ellipsis.tooltip"]
        }) : {
          ..._.tooltip,
          title: r["ellipsis.tooltip.title"] ? /* @__PURE__ */ b.jsx(T, {
            slot: r["ellipsis.tooltip.title"]
          }) : (d = _.tooltip) == null ? void 0 : d.title
        }
      } : void 0,
      children: S.length > 0 ? u : c
    })]
  });
});
export {
  pt as TypographyBase,
  pt as default
};
