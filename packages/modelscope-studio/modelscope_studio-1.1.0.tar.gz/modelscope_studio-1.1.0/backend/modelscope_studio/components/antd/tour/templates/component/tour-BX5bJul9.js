import { i as de, a as A, r as fe, g as me, w as O, b as pe } from "./Index-B3z39oMF.js";
const v = window.ms_globals.React, ie = window.ms_globals.React.forwardRef, ce = window.ms_globals.React.useRef, ae = window.ms_globals.React.useState, ue = window.ms_globals.React.useEffect, $ = window.ms_globals.React.useMemo, W = window.ms_globals.ReactDOM.createPortal, _e = window.ms_globals.internalContext.useContextPropsContext, P = window.ms_globals.internalContext.ContextPropsProvider, he = window.ms_globals.antd.Tour, ge = window.ms_globals.createItemsContext.createItemsContext;
var be = /\s/;
function we(e) {
  for (var t = e.length; t-- && be.test(e.charAt(t)); )
    ;
  return t;
}
var xe = /^\s+/;
function ye(e) {
  return e && e.slice(0, we(e) + 1).replace(xe, "");
}
var B = NaN, Ee = /^[-+]0x[0-9a-f]+$/i, ve = /^0b[01]+$/i, Ce = /^0o[0-7]+$/i, Ie = parseInt;
function H(e) {
  if (typeof e == "number")
    return e;
  if (de(e))
    return B;
  if (A(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = A(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = ye(e);
  var s = ve.test(e);
  return s || Ce.test(e) ? Ie(e.slice(2), s ? 2 : 8) : Ee.test(e) ? B : +e;
}
var F = function() {
  return fe.Date.now();
}, Re = "Expected a function", Se = Math.max, Oe = Math.min;
function ke(e, t, s) {
  var l, o, n, r, i, a, b = 0, h = !1, c = !1, m = !0;
  if (typeof e != "function")
    throw new TypeError(Re);
  t = H(t) || 0, A(s) && (h = !!s.leading, c = "maxWait" in s, n = c ? Se(H(s.maxWait) || 0, t) : n, m = "trailing" in s ? !!s.trailing : m);
  function u(_) {
    var E = l, S = o;
    return l = o = void 0, b = _, r = e.apply(S, E), r;
  }
  function w(_) {
    return b = _, i = setTimeout(g, t), h ? u(_) : r;
  }
  function f(_) {
    var E = _ - a, S = _ - b, U = t - E;
    return c ? Oe(U, n - S) : U;
  }
  function p(_) {
    var E = _ - a, S = _ - b;
    return a === void 0 || E >= t || E < 0 || c && S >= n;
  }
  function g() {
    var _ = F();
    if (p(_))
      return y(_);
    i = setTimeout(g, f(_));
  }
  function y(_) {
    return i = void 0, m && l ? u(_) : (l = o = void 0, r);
  }
  function C() {
    i !== void 0 && clearTimeout(i), b = 0, l = a = o = i = void 0;
  }
  function d() {
    return i === void 0 ? r : y(F());
  }
  function I() {
    var _ = F(), E = p(_);
    if (l = arguments, o = this, a = _, E) {
      if (i === void 0)
        return w(a);
      if (c)
        return clearTimeout(i), i = setTimeout(g, t), u(a);
    }
    return i === void 0 && (i = setTimeout(g, t)), r;
  }
  return I.cancel = C, I.flush = d, I;
}
var ee = {
  exports: {}
}, L = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Te = v, Pe = Symbol.for("react.element"), je = Symbol.for("react.fragment"), Le = Object.prototype.hasOwnProperty, Fe = Te.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Ne = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function te(e, t, s) {
  var l, o = {}, n = null, r = null;
  s !== void 0 && (n = "" + s), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (l in t) Le.call(t, l) && !Ne.hasOwnProperty(l) && (o[l] = t[l]);
  if (e && e.defaultProps) for (l in t = e.defaultProps, t) o[l] === void 0 && (o[l] = t[l]);
  return {
    $$typeof: Pe,
    type: e,
    key: n,
    ref: r,
    props: o,
    _owner: Fe.current
  };
}
L.Fragment = je;
L.jsx = te;
L.jsxs = te;
ee.exports = L;
var x = ee.exports;
const {
  SvelteComponent: We,
  assign: z,
  binding_callbacks: G,
  check_outros: Ae,
  children: ne,
  claim_element: re,
  claim_space: Me,
  component_subscribe: q,
  compute_slots: De,
  create_slot: Ue,
  detach: R,
  element: oe,
  empty: V,
  exclude_internal_props: J,
  get_all_dirty_from_scope: Be,
  get_slot_changes: He,
  group_outros: ze,
  init: Ge,
  insert_hydration: k,
  safe_not_equal: qe,
  set_custom_element_data: se,
  space: Ve,
  transition_in: T,
  transition_out: M,
  update_slot_base: Je
} = window.__gradio__svelte__internal, {
  beforeUpdate: Xe,
  getContext: Ye,
  onDestroy: Ke,
  setContext: Qe
} = window.__gradio__svelte__internal;
function X(e) {
  let t, s;
  const l = (
    /*#slots*/
    e[7].default
  ), o = Ue(
    l,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = oe("svelte-slot"), o && o.c(), this.h();
    },
    l(n) {
      t = re(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ne(t);
      o && o.l(r), r.forEach(R), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      k(n, t, r), o && o.m(t, null), e[9](t), s = !0;
    },
    p(n, r) {
      o && o.p && (!s || r & /*$$scope*/
      64) && Je(
        o,
        l,
        n,
        /*$$scope*/
        n[6],
        s ? He(
          l,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Be(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      s || (T(o, n), s = !0);
    },
    o(n) {
      M(o, n), s = !1;
    },
    d(n) {
      n && R(t), o && o.d(n), e[9](null);
    }
  };
}
function Ze(e) {
  let t, s, l, o, n = (
    /*$$slots*/
    e[4].default && X(e)
  );
  return {
    c() {
      t = oe("react-portal-target"), s = Ve(), n && n.c(), l = V(), this.h();
    },
    l(r) {
      t = re(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ne(t).forEach(R), s = Me(r), n && n.l(r), l = V(), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      k(r, t, i), e[8](t), k(r, s, i), n && n.m(r, i), k(r, l, i), o = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && T(n, 1)) : (n = X(r), n.c(), T(n, 1), n.m(l.parentNode, l)) : n && (ze(), M(n, 1, 1, () => {
        n = null;
      }), Ae());
    },
    i(r) {
      o || (T(n), o = !0);
    },
    o(r) {
      M(n), o = !1;
    },
    d(r) {
      r && (R(t), R(s), R(l)), e[8](null), n && n.d(r);
    }
  };
}
function Y(e) {
  const {
    svelteInit: t,
    ...s
  } = e;
  return s;
}
function $e(e, t, s) {
  let l, o, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const i = De(n);
  let {
    svelteInit: a
  } = t;
  const b = O(Y(t)), h = O();
  q(e, h, (d) => s(0, l = d));
  const c = O();
  q(e, c, (d) => s(1, o = d));
  const m = [], u = Ye("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: f,
    subSlotIndex: p
  } = me() || {}, g = a({
    parent: u,
    props: b,
    target: h,
    slot: c,
    slotKey: w,
    slotIndex: f,
    subSlotIndex: p,
    onDestroy(d) {
      m.push(d);
    }
  });
  Qe("$$ms-gr-react-wrapper", g), Xe(() => {
    b.set(Y(t));
  }), Ke(() => {
    m.forEach((d) => d());
  });
  function y(d) {
    G[d ? "unshift" : "push"](() => {
      l = d, h.set(l);
    });
  }
  function C(d) {
    G[d ? "unshift" : "push"](() => {
      o = d, c.set(o);
    });
  }
  return e.$$set = (d) => {
    s(17, t = z(z({}, t), J(d))), "svelteInit" in d && s(5, a = d.svelteInit), "$$scope" in d && s(6, r = d.$$scope);
  }, t = J(t), [l, o, h, c, i, a, r, n, y, C];
}
class et extends We {
  constructor(t) {
    super(), Ge(this, t, $e, Ze, qe, {
      svelteInit: 5
    });
  }
}
const K = window.ms_globals.rerender, N = window.ms_globals.tree;
function tt(e, t = {}) {
  function s(l) {
    const o = O(), n = new et({
      ...l,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, a = r.parent ?? N;
          return a.nodes = [...a.nodes, i], K({
            createPortal: W,
            node: N
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((b) => b.svelteInstance !== o), K({
              createPortal: W,
              node: N
            });
          }), i;
        },
        ...l.props
      }
    });
    return o.set(n), n;
  }
  return new Promise((l) => {
    window.ms_globals.initializePromise.then(() => {
      l(s);
    });
  });
}
const nt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function rt(e) {
  return e ? Object.keys(e).reduce((t, s) => {
    const l = e[s];
    return t[s] = ot(s, l), t;
  }, {}) : {};
}
function ot(e, t) {
  return typeof t == "number" && !nt.includes(e) ? t + "px" : t;
}
function D(e) {
  const t = [], s = e.cloneNode(!1);
  if (e._reactElement) {
    const o = v.Children.toArray(e._reactElement.props.children).map((n) => {
      if (v.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = D(n.props.el);
        return v.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...v.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return o.originalChildren = e._reactElement.props.children, t.push(W(v.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: o
    }), s)), {
      clonedElement: s,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((o) => {
    e.getEventListeners(o).forEach(({
      listener: r,
      type: i,
      useCapture: a
    }) => {
      s.addEventListener(i, r, a);
    });
  });
  const l = Array.from(e.childNodes);
  for (let o = 0; o < l.length; o++) {
    const n = l[o];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = D(n);
      t.push(...i), s.appendChild(r);
    } else n.nodeType === 3 && s.appendChild(n.cloneNode());
  }
  return {
    clonedElement: s,
    portals: t
  };
}
function st(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const j = ie(({
  slot: e,
  clone: t,
  className: s,
  style: l,
  observeAttributes: o
}, n) => {
  const r = ce(), [i, a] = ae([]), {
    forceClone: b
  } = _e(), h = b ? !0 : t;
  return ue(() => {
    var w;
    if (!r.current || !e)
      return;
    let c = e;
    function m() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), st(n, f), s && f.classList.add(...s.split(" ")), l) {
        const p = rt(l);
        Object.keys(p).forEach((g) => {
          f.style[g] = p[g];
        });
      }
    }
    let u = null;
    if (h && window.MutationObserver) {
      let f = function() {
        var C, d, I;
        (C = r.current) != null && C.contains(c) && ((d = r.current) == null || d.removeChild(c));
        const {
          portals: g,
          clonedElement: y
        } = D(e);
        c = y, a(g), c.style.display = "contents", m(), (I = r.current) == null || I.appendChild(c);
      };
      f();
      const p = ke(() => {
        f(), u == null || u.disconnect(), u == null || u.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      u = new window.MutationObserver(p), u.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", m(), (w = r.current) == null || w.appendChild(c);
    return () => {
      var f, p;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((p = r.current) == null || p.removeChild(c)), u == null || u.disconnect();
    };
  }, [e, h, s, l, n, o]), v.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function lt(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function it(e, t = !1) {
  try {
    if (pe(e))
      return e;
    if (t && !lt(e))
      return;
    if (typeof e == "string") {
      let s = e.trim();
      return s.startsWith(";") && (s = s.slice(1)), s.endsWith(";") && (s = s.slice(0, -1)), new Function(`return (...args) => (${s})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function Q(e, t) {
  return $(() => it(e, t), [e, t]);
}
function le(e, t, s) {
  const l = e.filter(Boolean);
  if (l.length !== 0)
    return l.map((o, n) => {
      var b;
      if (typeof o != "object")
        return o;
      const r = {
        ...o.props,
        key: ((b = o.props) == null ? void 0 : b.key) ?? (s ? `${s}-${n}` : `${n}`)
      };
      let i = r;
      Object.keys(o.slots).forEach((h) => {
        if (!o.slots[h] || !(o.slots[h] instanceof Element) && !o.slots[h].el)
          return;
        const c = h.split(".");
        c.forEach((g, y) => {
          i[g] || (i[g] = {}), y !== c.length - 1 && (i = r[g]);
        });
        const m = o.slots[h];
        let u, w, f = !1, p = t == null ? void 0 : t.forceClone;
        m instanceof Element ? u = m : (u = m.el, w = m.callback, f = m.clone ?? f, p = m.forceClone ?? p), p = p ?? !!w, i[c[c.length - 1]] = u ? w ? (...g) => (w(c[c.length - 1], g), /* @__PURE__ */ x.jsx(P, {
          params: g,
          forceClone: p,
          children: /* @__PURE__ */ x.jsx(j, {
            slot: u,
            clone: f
          })
        })) : /* @__PURE__ */ x.jsx(P, {
          forceClone: p,
          children: /* @__PURE__ */ x.jsx(j, {
            slot: u,
            clone: f
          })
        }) : i[c[c.length - 1]], i = r;
      });
      const a = "children";
      return o[a] && (r[a] = le(o[a], t, `${n}`)), r;
    });
}
function Z(e, t) {
  return e ? /* @__PURE__ */ x.jsx(j, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function ct({
  key: e,
  slots: t,
  targets: s
}, l) {
  return t[e] ? (...o) => s ? s.map((n, r) => /* @__PURE__ */ x.jsx(P, {
    params: o,
    forceClone: !0,
    children: Z(n, {
      clone: !0,
      ...l
    })
  }, r)) : /* @__PURE__ */ x.jsx(P, {
    params: o,
    forceClone: !0,
    children: Z(t[e], {
      clone: !0,
      ...l
    })
  }) : void 0;
}
const {
  withItemsContextProvider: at,
  useItems: ut,
  ItemHandler: ft
} = ge("antd-tour-items"), mt = tt(at(["steps", "default"], ({
  slots: e,
  steps: t,
  children: s,
  onChange: l,
  onClose: o,
  getPopupContainer: n,
  setSlotParams: r,
  indicatorsRender: i,
  ...a
}) => {
  const b = Q(n), h = Q(i), {
    items: c
  } = ut(), m = c.steps.length > 0 ? c.steps : c.default;
  return /* @__PURE__ */ x.jsxs(x.Fragment, {
    children: [/* @__PURE__ */ x.jsx("div", {
      style: {
        display: "none"
      },
      children: s
    }), /* @__PURE__ */ x.jsx(he, {
      ...a,
      steps: $(() => t || le(m), [t, m]),
      onChange: (u) => {
        l == null || l(u);
      },
      closeIcon: e.closeIcon ? /* @__PURE__ */ x.jsx(j, {
        slot: e.closeIcon
      }) : a.closeIcon,
      indicatorsRender: e.indicatorsRender ? ct({
        slots: e,
        setSlotParams: r,
        key: "indicatorsRender"
      }) : h,
      getPopupContainer: b,
      onClose: (u, ...w) => {
        o == null || o(u, ...w);
      }
    })]
  });
}));
export {
  mt as Tour,
  mt as default
};
