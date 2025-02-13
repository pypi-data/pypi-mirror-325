import { i as ue, a as N, r as de, g as fe, w as P, b as me } from "./Index-HyGpwriz.js";
const E = window.ms_globals.React, ie = window.ms_globals.React.forwardRef, le = window.ms_globals.React.useRef, ce = window.ms_globals.React.useState, ae = window.ms_globals.React.useEffect, $ = window.ms_globals.React.useMemo, F = window.ms_globals.ReactDOM.createPortal, pe = window.ms_globals.internalContext.useContextPropsContext, U = window.ms_globals.internalContext.ContextPropsProvider, _e = window.ms_globals.antd.Slider, he = window.ms_globals.createItemsContext.createItemsContext;
var ge = /\s/;
function be(e) {
  for (var t = e.length; t-- && ge.test(e.charAt(t)); )
    ;
  return t;
}
var we = /^\s+/;
function xe(e) {
  return e && e.slice(0, be(e) + 1).replace(we, "");
}
var G = NaN, ye = /^[-+]0x[0-9a-f]+$/i, Ee = /^0b[01]+$/i, Ce = /^0o[0-7]+$/i, Ie = parseInt;
function H(e) {
  if (typeof e == "number")
    return e;
  if (ue(e))
    return G;
  if (N(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = N(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = xe(e);
  var n = Ee.test(e);
  return n || Ce.test(e) ? Ie(e.slice(2), n ? 2 : 8) : ye.test(e) ? G : +e;
}
var L = function() {
  return de.Date.now();
}, Se = "Expected a function", Re = Math.max, ke = Math.min;
function Pe(e, t, n) {
  var s, i, r, o, l, u, p = 0, _ = !1, c = !1, g = !0;
  if (typeof e != "function")
    throw new TypeError(Se);
  t = H(t) || 0, N(n) && (_ = !!n.leading, c = "maxWait" in n, r = c ? Re(H(n.maxWait) || 0, t) : r, g = "trailing" in n ? !!n.trailing : g);
  function d(f) {
    var y = s, k = i;
    return s = i = void 0, p = f, o = e.apply(k, y), o;
  }
  function w(f) {
    return p = f, l = setTimeout(b, t), _ ? d(f) : o;
  }
  function m(f) {
    var y = f - u, k = f - p, D = t - y;
    return c ? ke(D, r - k) : D;
  }
  function h(f) {
    var y = f - u, k = f - p;
    return u === void 0 || y >= t || y < 0 || c && k >= r;
  }
  function b() {
    var f = L();
    if (h(f))
      return C(f);
    l = setTimeout(b, m(f));
  }
  function C(f) {
    return l = void 0, g && s ? d(f) : (s = i = void 0, o);
  }
  function I() {
    l !== void 0 && clearTimeout(l), p = 0, s = u = i = l = void 0;
  }
  function a() {
    return l === void 0 ? o : C(L());
  }
  function S() {
    var f = L(), y = h(f);
    if (s = arguments, i = this, u = f, y) {
      if (l === void 0)
        return w(u);
      if (c)
        return clearTimeout(l), l = setTimeout(b, t), d(u);
    }
    return l === void 0 && (l = setTimeout(b, t)), o;
  }
  return S.cancel = I, S.flush = a, S;
}
var ee = {
  exports: {}
}, v = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Oe = E, Te = Symbol.for("react.element"), ve = Symbol.for("react.fragment"), Le = Object.prototype.hasOwnProperty, je = Oe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Fe = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function te(e, t, n) {
  var s, i = {}, r = null, o = null;
  n !== void 0 && (r = "" + n), t.key !== void 0 && (r = "" + t.key), t.ref !== void 0 && (o = t.ref);
  for (s in t) Le.call(t, s) && !Fe.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: Te,
    type: e,
    key: r,
    ref: o,
    props: i,
    _owner: je.current
  };
}
v.Fragment = ve;
v.jsx = te;
v.jsxs = te;
ee.exports = v;
var x = ee.exports;
const {
  SvelteComponent: Ne,
  assign: z,
  binding_callbacks: B,
  check_outros: We,
  children: ne,
  claim_element: re,
  claim_space: Ae,
  component_subscribe: K,
  compute_slots: Me,
  create_slot: De,
  detach: R,
  element: oe,
  empty: q,
  exclude_internal_props: V,
  get_all_dirty_from_scope: Ue,
  get_slot_changes: Ge,
  group_outros: He,
  init: ze,
  insert_hydration: O,
  safe_not_equal: Be,
  set_custom_element_data: se,
  space: Ke,
  transition_in: T,
  transition_out: W,
  update_slot_base: qe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ve,
  getContext: Je,
  onDestroy: Xe,
  setContext: Ye
} = window.__gradio__svelte__internal;
function J(e) {
  let t, n;
  const s = (
    /*#slots*/
    e[7].default
  ), i = De(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = oe("svelte-slot"), i && i.c(), this.h();
    },
    l(r) {
      t = re(r, "SVELTE-SLOT", {
        class: !0
      });
      var o = ne(t);
      i && i.l(o), o.forEach(R), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
    },
    m(r, o) {
      O(r, t, o), i && i.m(t, null), e[9](t), n = !0;
    },
    p(r, o) {
      i && i.p && (!n || o & /*$$scope*/
      64) && qe(
        i,
        s,
        r,
        /*$$scope*/
        r[6],
        n ? Ge(
          s,
          /*$$scope*/
          r[6],
          o,
          null
        ) : Ue(
          /*$$scope*/
          r[6]
        ),
        null
      );
    },
    i(r) {
      n || (T(i, r), n = !0);
    },
    o(r) {
      W(i, r), n = !1;
    },
    d(r) {
      r && R(t), i && i.d(r), e[9](null);
    }
  };
}
function Qe(e) {
  let t, n, s, i, r = (
    /*$$slots*/
    e[4].default && J(e)
  );
  return {
    c() {
      t = oe("react-portal-target"), n = Ke(), r && r.c(), s = q(), this.h();
    },
    l(o) {
      t = re(o, "REACT-PORTAL-TARGET", {
        class: !0
      }), ne(t).forEach(R), n = Ae(o), r && r.l(o), s = q(), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
    },
    m(o, l) {
      O(o, t, l), e[8](t), O(o, n, l), r && r.m(o, l), O(o, s, l), i = !0;
    },
    p(o, [l]) {
      /*$$slots*/
      o[4].default ? r ? (r.p(o, l), l & /*$$slots*/
      16 && T(r, 1)) : (r = J(o), r.c(), T(r, 1), r.m(s.parentNode, s)) : r && (He(), W(r, 1, 1, () => {
        r = null;
      }), We());
    },
    i(o) {
      i || (T(r), i = !0);
    },
    o(o) {
      W(r), i = !1;
    },
    d(o) {
      o && (R(t), R(n), R(s)), e[8](null), r && r.d(o);
    }
  };
}
function X(e) {
  const {
    svelteInit: t,
    ...n
  } = e;
  return n;
}
function Ze(e, t, n) {
  let s, i, {
    $$slots: r = {},
    $$scope: o
  } = t;
  const l = Me(r);
  let {
    svelteInit: u
  } = t;
  const p = P(X(t)), _ = P();
  K(e, _, (a) => n(0, s = a));
  const c = P();
  K(e, c, (a) => n(1, i = a));
  const g = [], d = Je("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: m,
    subSlotIndex: h
  } = fe() || {}, b = u({
    parent: d,
    props: p,
    target: _,
    slot: c,
    slotKey: w,
    slotIndex: m,
    subSlotIndex: h,
    onDestroy(a) {
      g.push(a);
    }
  });
  Ye("$$ms-gr-react-wrapper", b), Ve(() => {
    p.set(X(t));
  }), Xe(() => {
    g.forEach((a) => a());
  });
  function C(a) {
    B[a ? "unshift" : "push"](() => {
      s = a, _.set(s);
    });
  }
  function I(a) {
    B[a ? "unshift" : "push"](() => {
      i = a, c.set(i);
    });
  }
  return e.$$set = (a) => {
    n(17, t = z(z({}, t), V(a))), "svelteInit" in a && n(5, u = a.svelteInit), "$$scope" in a && n(6, o = a.$$scope);
  }, t = V(t), [s, i, _, c, l, u, o, r, C, I];
}
class $e extends Ne {
  constructor(t) {
    super(), ze(this, t, Ze, Qe, Be, {
      svelteInit: 5
    });
  }
}
const Y = window.ms_globals.rerender, j = window.ms_globals.tree;
function et(e, t = {}) {
  function n(s) {
    const i = P(), r = new $e({
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
          }, u = o.parent ?? j;
          return u.nodes = [...u.nodes, l], Y({
            createPortal: F,
            node: j
          }), o.onDestroy(() => {
            u.nodes = u.nodes.filter((p) => p.svelteInstance !== i), Y({
              createPortal: F,
              node: j
            });
          }), l;
        },
        ...s.props
      }
    });
    return i.set(r), r;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(n);
    });
  });
}
const tt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function nt(e) {
  return e ? Object.keys(e).reduce((t, n) => {
    const s = e[n];
    return t[n] = rt(n, s), t;
  }, {}) : {};
}
function rt(e, t) {
  return typeof t == "number" && !tt.includes(e) ? t + "px" : t;
}
function A(e) {
  const t = [], n = e.cloneNode(!1);
  if (e._reactElement) {
    const i = E.Children.toArray(e._reactElement.props.children).map((r) => {
      if (E.isValidElement(r) && r.props.__slot__) {
        const {
          portals: o,
          clonedElement: l
        } = A(r.props.el);
        return E.cloneElement(r, {
          ...r.props,
          el: l,
          children: [...E.Children.toArray(r.props.children), ...o]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(F(E.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), n)), {
      clonedElement: n,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: o,
      type: l,
      useCapture: u
    }) => {
      n.addEventListener(l, o, u);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const r = s[i];
    if (r.nodeType === 1) {
      const {
        clonedElement: o,
        portals: l
      } = A(r);
      t.push(...l), n.appendChild(o);
    } else r.nodeType === 3 && n.appendChild(r.cloneNode());
  }
  return {
    clonedElement: n,
    portals: t
  };
}
function ot(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const M = ie(({
  slot: e,
  clone: t,
  className: n,
  style: s,
  observeAttributes: i
}, r) => {
  const o = le(), [l, u] = ce([]), {
    forceClone: p
  } = pe(), _ = p ? !0 : t;
  return ae(() => {
    var w;
    if (!o.current || !e)
      return;
    let c = e;
    function g() {
      let m = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (m = c.children[0], m.tagName.toLowerCase() === "react-portal-target" && m.children[0] && (m = m.children[0])), ot(r, m), n && m.classList.add(...n.split(" ")), s) {
        const h = nt(s);
        Object.keys(h).forEach((b) => {
          m.style[b] = h[b];
        });
      }
    }
    let d = null;
    if (_ && window.MutationObserver) {
      let m = function() {
        var I, a, S;
        (I = o.current) != null && I.contains(c) && ((a = o.current) == null || a.removeChild(c));
        const {
          portals: b,
          clonedElement: C
        } = A(e);
        c = C, u(b), c.style.display = "contents", g(), (S = o.current) == null || S.appendChild(c);
      };
      m();
      const h = Pe(() => {
        m(), d == null || d.disconnect(), d == null || d.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      d = new window.MutationObserver(h), d.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", g(), (w = o.current) == null || w.appendChild(c);
    return () => {
      var m, h;
      c.style.display = "", (m = o.current) != null && m.contains(c) && ((h = o.current) == null || h.removeChild(c)), d == null || d.disconnect();
    };
  }, [e, _, n, s, r, i]), E.createElement("react-child", {
    ref: o,
    style: {
      display: "contents"
    }
  }, ...l);
});
function st(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function it(e, t = !1) {
  try {
    if (me(e))
      return e;
    if (t && !st(e))
      return;
    if (typeof e == "string") {
      let n = e.trim();
      return n.startsWith(";") && (n = n.slice(1)), n.endsWith(";") && (n = n.slice(0, -1)), new Function(`return (...args) => (${n})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function Q(e, t) {
  return $(() => it(e, t), [e, t]);
}
function Z(e, t) {
  return e ? /* @__PURE__ */ x.jsx(M, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function lt({
  key: e,
  slots: t,
  targets: n
}, s) {
  return t[e] ? (...i) => n ? n.map((r, o) => /* @__PURE__ */ x.jsx(U, {
    params: i,
    forceClone: !0,
    children: Z(r, {
      clone: !0,
      ...s
    })
  }, o)) : /* @__PURE__ */ x.jsx(U, {
    params: i,
    forceClone: !0,
    children: Z(t[e], {
      clone: !0,
      ...s
    })
  }) : void 0;
}
const {
  withItemsContextProvider: ct,
  useItems: at,
  ItemHandler: ft
} = he("antd-slider-marks"), ut = (e) => e.reduce((t, n) => {
  const s = n == null ? void 0 : n.props.number;
  return s !== void 0 && (t[s] = (n == null ? void 0 : n.slots.label) instanceof Element ? {
    ...n.props,
    label: /* @__PURE__ */ x.jsx(M, {
      slot: n == null ? void 0 : n.slots.label
    })
  } : (n == null ? void 0 : n.slots.children) instanceof Element ? /* @__PURE__ */ x.jsx(M, {
    slot: n == null ? void 0 : n.slots.children
  }) : {
    ...n == null ? void 0 : n.props
  }), t;
}, {}), mt = et(ct(["marks"], ({
  marks: e,
  children: t,
  onValueChange: n,
  onChange: s,
  elRef: i,
  tooltip: r,
  step: o,
  slots: l,
  setSlotParams: u,
  ...p
}) => {
  const _ = (w) => {
    s == null || s(w), n(w);
  }, c = Q(r == null ? void 0 : r.getPopupContainer), g = Q(r == null ? void 0 : r.formatter), {
    items: {
      marks: d
    }
  } = at();
  return /* @__PURE__ */ x.jsxs(x.Fragment, {
    children: [/* @__PURE__ */ x.jsx("div", {
      style: {
        display: "none"
      },
      children: t
    }), /* @__PURE__ */ x.jsx(_e, {
      ...p,
      tooltip: {
        ...r,
        getPopupContainer: c,
        formatter: l["tooltip.formatter"] ? lt({
          key: "tooltip.formatter",
          setSlotParams: u,
          slots: l
        }) : g
      },
      marks: $(() => e || ut(d), [d, e]),
      step: o === void 0 ? null : o,
      ref: i,
      onChange: _
    })]
  });
}));
export {
  mt as Slider,
  mt as default
};
